import { memo, useMemo } from "react";
import { Globe, ExternalLink } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";

type WebVariant = "WebSearch" | "WebFetch";

interface WebSearchInput {
  query?: string;
  url?: string;
  prompt?: string;
}

interface WebSearchProps extends ToolComponentProps {
  variant: WebVariant;
}

function truncateUrl(url: string, max = 80): string {
  if (url.length <= max) return url;
  return url.slice(0, max) + "...";
}

const variantConfig: Record<
  WebVariant,
  { icon: React.ReactNode; label: string }
> = {
  WebSearch: {
    icon: <Globe className="h-3.5 w-3.5" />,
    label: "Search",
  },
  WebFetch: {
    icon: <ExternalLink className="h-3.5 w-3.5" />,
    label: "Fetch",
  },
};

const WebSearchToolInner: React.FC<WebSearchProps> = ({ block, variant }) => {
  const config = variantConfig[variant];
  const input = useMemo(
    () => safeParseJson<WebSearchInput>(block.input, {}),
    [block.input],
  );

  const title = useMemo(() => {
    if (variant === "WebSearch") {
      return input.query ? `${config.label}: ${input.query}` : `${config.label}...`;
    }
    return input.url ? truncateUrl(input.url) : `${config.label}...`;
  }, [variant, input.query, input.url, config.label]);

  const hasPrompt = variant === "WebFetch" && Boolean(input.prompt);

  return (
    <ToolCard
      icon={config.icon}
      status={block.status}
      title={title}
      expandable={hasPrompt}
    >
      {hasPrompt && (
        <div className="text-[11px] text-gray-500">
          <span className="text-gray-400">Prompt: </span>
          {input.prompt}
        </div>
      )}
    </ToolCard>
  );
};

const WebSearchToolMemo = memo(WebSearchToolInner);

/** Pre-bound variants for the registry */
export const WebSearchVariant: React.FC<ToolComponentProps> = (props) => (
  <WebSearchToolMemo {...props} variant="WebSearch" />
);
export const WebFetchVariant: React.FC<ToolComponentProps> = (props) => (
  <WebSearchToolMemo {...props} variant="WebFetch" />
);
