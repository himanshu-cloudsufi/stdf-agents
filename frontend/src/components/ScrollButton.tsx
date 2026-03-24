import { memo } from "react";
import { ChevronDown } from "lucide-react";

interface ScrollButtonProps {
  onClick: () => void;
}

export const ScrollButton = memo(function ScrollButton({
  onClick,
}: ScrollButtonProps) {
  return (
    <div className="absolute inset-x-0 bottom-full flex justify-center pb-2">
      <button
        onClick={onClick}
        className="flex h-8 w-8 items-center justify-center rounded-full border border-gray-200 bg-white shadow-md transition-transform duration-200 ease-out hover:scale-110 hover:bg-gray-50 active:scale-95"
        aria-label="Scroll to bottom"
      >
        <ChevronDown className="h-4 w-4 text-gray-500" />
      </button>
    </div>
  );
});
