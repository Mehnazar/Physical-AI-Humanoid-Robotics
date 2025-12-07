#!/usr/bin/env node
/**
 * Check links in Physical AI & Humanoid Robotics Book
 *
 * This script validates all links in Markdown files:
 * - Parses all Markdown files in book/docs/
 * - Extracts internal links (to other markdown files)
 * - Extracts external links (to websites, documentation)
 * - Verifies internal links point to existing files
 * - Verifies external links return HTTP 200 (with timeout)
 * - Reports broken links
 *
 * Reference: specs/001-physical-ai-book/plan.md:174, tasks.md:T075
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const DOCS_DIR = path.join(__dirname, '../book/docs');
const TIMEOUT_MS = 5000;

// Extract markdown links [text](url)
function extractLinks(content) {
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
  const links = [];
  let match;

  while ((match = linkRegex.exec(content)) !== null) {
    links.push({
      text: match[1],
      url: match[2],
    });
  }

  return links;
}

// Check if internal link exists
function checkInternalLink(linkUrl, sourceFile) {
  const sourcePath = path.dirname(sourceFile);
  const targetPath = path.resolve(sourcePath, linkUrl);

  return fs.existsSync(targetPath);
}

// Check external link (HTTP request)
function checkExternalLink(url) {
  return new Promise((resolve) => {
    const protocol = url.startsWith('https') ? https : http;
    const req = protocol.get(url, { timeout: TIMEOUT_MS }, (res) => {
      resolve({ url, status: res.statusCode, ok: res.statusCode === 200 });
    });

    req.on('error', (error) => {
      resolve({ url, status: 'error', ok: false, error: error.message });
    });

    req.on('timeout', () => {
      req.destroy();
      resolve({ url, status: 'timeout', ok: false });
    });
  });
}

// Get all markdown files
function getMarkdownFiles(dir) {
  const files = [];

  function traverse(currentDir) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(currentDir, entry.name);

      if (entry.isDirectory()) {
        traverse(fullPath);
      } else if (entry.isFile() && (entry.name.endsWith('.md') || entry.name.endsWith('.mdx'))) {
        files.push(fullPath);
      }
    }
  }

  traverse(dir);
  return files;
}

async function main() {
  if (!fs.existsSync(DOCS_DIR)) {
    console.error('Error: book/docs/ directory not found');
    process.exit(1);
  }

  const markdownFiles = getMarkdownFiles(DOCS_DIR);

  if (markdownFiles.length === 0) {
    console.log('No markdown files found in book/docs/');
    return;
  }

  console.log(`Checking links in ${markdownFiles.length} markdown files...\n`);

  let totalLinks = 0;
  let brokenInternalLinks = [];
  let brokenExternalLinks = [];

  for (const file of markdownFiles) {
    const content = fs.readFileSync(file, 'utf-8');
    const links = extractLinks(content);
    totalLinks += links.length;

    const relativePath = path.relative(path.join(__dirname, '..'), file);

    for (const link of links) {
      if (link.url.startsWith('http://') || link.url.startsWith('https://')) {
        // External link - check HTTP
        const result = await checkExternalLink(link.url);
        if (!result.ok) {
          brokenExternalLinks.push({
            file: relativePath,
            ...result,
          });
        }
      } else if (!link.url.startsWith('#') && !link.url.startsWith('mailto:')) {
        // Internal link - check file exists
        if (!checkInternalLink(link.url, file)) {
          brokenInternalLinks.push({
            file: relativePath,
            url: link.url,
          });
        }
      }
    }
  }

  console.log('='.repeat(60));
  console.log(`Link validation complete:`);
  console.log(`  Total links: ${totalLinks}`);
  console.log(`  Broken internal links: ${brokenInternalLinks.length}`);
  console.log(`  Broken external links: ${brokenExternalLinks.length}`);

  if (brokenInternalLinks.length > 0) {
    console.log(`\n❌ Broken internal links:`);
    for (const link of brokenInternalLinks) {
      console.log(`   ${link.file} -> ${link.url}`);
    }
  }

  if (brokenExternalLinks.length > 0) {
    console.log(`\n❌ Broken external links:`);
    for (const link of brokenExternalLinks) {
      console.log(
        `   ${link.file} -> ${link.url} (${link.status}${link.error ? ': ' + link.error : ''})`
      );
    }
  }

  if (brokenInternalLinks.length === 0 && brokenExternalLinks.length === 0) {
    console.log('\n✅ All links are valid!');
  }

  process.exit(brokenInternalLinks.length > 0 ? 1 : 0);
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
