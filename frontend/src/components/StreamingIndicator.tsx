interface Props {
  visible: boolean;
}

export function StreamingIndicator({ visible }: Props) {
  if (!visible) return null;

  return (
    <div className="flex items-center gap-1 px-4 py-2 text-gray-400 text-sm">
      <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:0ms]" />
      <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:150ms]" />
      <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:300ms]" />
    </div>
  );
}
