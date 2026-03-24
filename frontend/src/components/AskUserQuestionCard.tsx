import { useState } from "react";

export interface QuestionOption {
  label: string;
  description: string;
  preview?: string;
}

export interface Question {
  question: string;
  header: string;
  options: QuestionOption[];
  multiSelect: boolean;
}

interface Props {
  questions: Question[];
  onAnswer: (answers: Record<string, string>) => void;
  answered: boolean;
}

export function AskUserQuestionCard({ questions, onAnswer, answered }: Props) {
  const [selections, setSelections] = useState<Record<string, Set<string>>>({});

  function toggleOption(question: string, label: string, multiSelect: boolean) {
    if (answered) return;
    setSelections((prev) => {
      const current = prev[question] || new Set();
      const next = new Set(current);
      if (multiSelect) {
        if (next.has(label)) next.delete(label);
        else next.add(label);
      } else {
        next.clear();
        next.add(label);
      }
      return { ...prev, [question]: next };
    });
  }

  function handleSubmit() {
    const answers: Record<string, string> = {};
    for (const q of questions) {
      const selected = selections[q.question];
      if (selected && selected.size > 0) {
        answers[q.question] = [...selected].join(", ");
      }
    }
    onAnswer(answers);
  }

  const allAnswered = questions.every(
    (q) => (selections[q.question]?.size ?? 0) > 0,
  );

  return (
    <div className="border-2 border-blue-200 rounded-xl bg-blue-50/50 p-4 my-3 space-y-4">
      {questions.map((q) => (
        <div key={q.question} className="space-y-2">
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold uppercase tracking-wider text-blue-600 bg-blue-100 px-2 py-0.5 rounded">
              {q.header}
            </span>
            {q.multiSelect && (
              <span className="text-xs text-gray-400">select multiple</span>
            )}
          </div>
          <p className="text-sm font-medium text-gray-800">{q.question}</p>
          <div className="grid gap-2">
            {q.options.map((opt) => {
              const selected = selections[q.question]?.has(opt.label);
              return (
                <button
                  key={opt.label}
                  onClick={() =>
                    toggleOption(q.question, opt.label, q.multiSelect)
                  }
                  disabled={answered}
                  className={`text-left px-4 py-3 rounded-lg border-2 transition-all cursor-pointer ${
                    selected
                      ? "border-blue-500 bg-blue-50 ring-1 ring-blue-500"
                      : "border-gray-200 bg-white hover:border-blue-300"
                  } ${answered ? "opacity-60 cursor-not-allowed" : ""}`}
                >
                  <div className="text-sm font-medium text-gray-800">
                    {opt.label}
                  </div>
                  {opt.description && (
                    <div className="text-xs text-gray-500 mt-0.5">
                      {opt.description}
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      ))}
      {!answered && (
        <button
          onClick={handleSubmit}
          disabled={!allAnswered}
          className="w-full px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors cursor-pointer"
        >
          Submit
        </button>
      )}
      {answered && (
        <div className="text-xs text-green-600 font-medium flex items-center gap-1">
          <span>✓</span> Answered
        </div>
      )}
    </div>
  );
}
