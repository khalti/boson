import { useRouterState } from "@tanstack/react-router";
import { useEffect, useState } from "react";

export function RouterProgressBar() {
  const isLoading = useRouterState({ select: (s) => s.status === "pending" });
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isLoading) {
      setProgress(10);
      interval = setInterval(() => {
        setProgress((p) => (p < 85 ? p + 5 : p));
      }, 100);
    } else {
      setProgress(100);
      const timeout = setTimeout(() => {
        setProgress(0);
      }, 200);
      return () => clearTimeout(timeout);
    }
    return () => clearInterval(interval);
  }, [isLoading]);

  if (progress === 0) return null;

  return (
    <div
      className="fixed top-0 left-0 h-1 bg-primary z-[9999] transition-all duration-200 ease-out"
      style={{ width: `${progress}%` }}
    />
  );
}
