import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type QuickLinkItem = {
  title: string;
  icon: string;
  description: string;
  link: string;
  color: string;
};

const quickLinks: QuickLinkItem[] = [
  {
    title: 'Introduction',
    icon: '📖',
    description: 'Start your journey into Physical AI',
    link: '/docs/intro',
    color: 'blue',
  },
  {
    title: 'AI Fundamentals',
    icon: '🧠',
    description: 'Core concepts of AI and ML',
    link: '/docs/intro',
    color: 'purple',
  },
  {
    title: 'Robotics Basics',
    icon: '🔧',
    description: 'Hardware and mechanical systems',
    link: '/docs/intro',
    color: 'orange',
  },
  {
    title: 'Code Examples',
    icon: '💻',
    description: 'Practical implementations',
    link: '/docs/intro',
    color: 'green',
  },
];

function QuickLinkCard({title, icon, description, link, color}: QuickLinkItem) {
  return (
    <Link to={link} className={clsx(styles.quickLinkCard, styles[`card${color}`])}>
      <div className={styles.cardIcon}>{icon}</div>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardDescription}>{description}</p>
      <div className={styles.cardArrow}>→</div>
    </Link>
  );
}

export default function QuickLinks(): ReactNode {
  return (
    <section className={styles.quickLinksSection}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Quick Start Guide</h2>
        <p className={styles.sectionSubtitle}>
          Choose your learning path and dive into the world of Physical AI and Humanoid Robotics
        </p>
        <div className={styles.quickLinksGrid}>
          {quickLinks.map((props, idx) => (
            <QuickLinkCard key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
