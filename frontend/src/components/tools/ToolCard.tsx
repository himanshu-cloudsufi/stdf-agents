import React, { useState, memo, type JSX } from "react";
import { Check, ChevronRight, Circle, Loader2, X } from "lucide-react";
import type { ToolCallBlock } from "../../types";

// ---------- shared prop types ----------

export interface ToolComponentProps {
  block: ToolCallBlock;
}

export type ToolCardStatus = "running" | "done" | "error";

type ToolCardTitle = string | ((status: ToolCardStatus) => string);

type Content = React.ReactNode | string | null | undefined;

interface ToolCardProps {
  icon: React.ReactNode;
  status: ToolCardStatus;
  title: ToolCardTitle;
  loadingContent?: Content;
  error?: Content;
  statusDetail?: Content;
  children?: React.ReactNode;
  className?: string;
  expandable?: boolean;
  defaultExpanded?: boolean;
}

export const statusIndicator: Record<ToolCardStatus, JSX.Element> = {
  done: <Check className="h-3 w-3 text-green-600" />,
  error: <X className="h-3 w-3 text-red-600" />,
  running: (
    <Circle className="h-3 w-3 animate-pulse text-gray-400" />
  ),
};

const ToolCardInner: React.FC<ToolCardProps> = ({
  icon,
  status,
  title,
  loadingContent,
  error,
  statusDetail,
  children,
  className = "",
  expandable = false,
  defaultExpanded = false,
}) => {
  const [expanded, setExpanded] = useState(defaultExpanded);
  const resolvedTitle = typeof title === "function" ? title(status) : title;

  const hasExpandableContent = expandable && children;
  const showChildren = !expandable || expanded;

  const header = (
    <div className="flex items-center gap-1.5">
      <div className="flex-shrink-0 text-gray-400">{icon}</div>
      <span
        className="max-w-md truncate text-xs text-gray-500"
        title={resolvedTitle}
      >
        {resolvedTitle}
      </span>
      {statusIndicator[status]}
      {hasExpandableContent && (
        <ChevronRight
          className={`h-3 w-3 text-gray-400 transition-transform duration-200 ${expanded ? "rotate-90" : ""}`}
        />
      )}
    </div>
  );

  const meta = (
    <>
      {status === "running" &&
        loadingContent &&
        (React.isValidElement(loadingContent) ? (
          loadingContent
        ) : (
          <p className="mt-0.5 pl-5 text-xs text-gray-400">
            {loadingContent}
          </p>
        ))}
      {status === "error" &&
        error &&
        (React.isValidElement(error) ? (
          error
        ) : (
          <p className="mt-0.5 pl-5 text-xs text-red-600">{error}</p>
        ))}
      {statusDetail &&
        (React.isValidElement(statusDetail) ? (
          statusDetail
        ) : (
          <p className="mt-0.5 pl-5 text-xs text-gray-400">{statusDetail}</p>
        ))}
    </>
  );

  return (
    <div className={`group/tool my-1 ${className}`}>
      <div className="flex items-center gap-1">
        {hasExpandableContent ? (
          <button
            type="button"
            onClick={() => setExpanded((prev) => !prev)}
            className="-ml-1 rounded-md px-1 py-0.5 text-left transition-colors duration-150 hover:bg-gray-50"
            aria-expanded={expanded}
          >
            {header}
          </button>
        ) : (
          <div className="-ml-1 px-1 py-0.5">{header}</div>
        )}
      </div>
      {meta}
      {showChildren && children && (
        <div className="mt-1.5 border-l border-gray-200 pl-3">{children}</div>
      )}
    </div>
  );
};

export const ToolCard = memo(ToolCardInner);

// Re-export Loader2 so downstream tool renderers can use it
export { Loader2 as LoaderIcon };
