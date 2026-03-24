interface Props {
  suggestions: string[];
  onSelect: (text: string) => void;
}

export function PromptSuggestions({ suggestions, onSelect }: Props) {
  if (suggestions.length === 0) return null;

  return (
    <div className="flex flex-wrap gap-1.5 mt-2">
      {suggestions.map((suggestion, i) => (
        <button
          key={i}
          type="button"
          onClick={() => onSelect(suggestion)}
          className="bg-white border border-gray-200 rounded-full px-3 py-1 text-xs hover:bg-gray-50 cursor-pointer transition-colors text-gray-700"
        >
          {suggestion}
        </button>
      ))}
    </div>
  );
}
