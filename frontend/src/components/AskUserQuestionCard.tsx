import { useState, useCallback, useMemo, useEffect } from "react";
import { HelpCircle, ChevronUp, ChevronDown } from "lucide-react";
import type { Question } from "../types";

const LETTER_OPTIONS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const OTHER_VALUE = "__other__";

interface Props {
  questions: Question[];
  answered: boolean;
  onAnswer: (answers: Record<string, string>) => void;
}

export function AskUserQuestionCard({ questions, answered, onAnswer }: Props) {
  const totalQuestions = questions.length;
  const [currentIndex, setCurrentIndex] = useState(0);
  const [formAnswers, setFormAnswers] = useState<Record<string, string | string[]>>({});
  const [otherInputs, setOtherInputs] = useState<Record<string, string>>({});

  // Reset state when questions change
  useEffect(() => {
    setCurrentIndex(0);
    setFormAnswers({});
    setOtherInputs({});
  }, [questions]);

  const currentQuestion = questions[currentIndex];
  const currentKey = `question_${currentIndex}`;
  const currentAnswer = formAnswers[currentKey];
  const isOtherSelected = Array.isArray(currentAnswer)
    ? currentAnswer.includes(OTHER_VALUE)
    : currentAnswer === OTHER_VALUE;

  const allQuestionsAnswered = useMemo(
    () =>
      questions.every((_, qIndex) => {
        const key = `question_${qIndex}`;
        const answer = formAnswers[key];
        const otherInput = otherInputs[key]?.trim();
        const isOther = Array.isArray(answer)
          ? answer.includes(OTHER_VALUE)
          : answer === OTHER_VALUE;
        if (isOther) return !!otherInput;
        return answer && (Array.isArray(answer) ? answer.length > 0 : true);
      }),
    [questions, formAnswers, otherInputs],
  );

  const isSelected = useCallback(
    (optionLabel: string) => {
      const answer = formAnswers[currentKey];
      if (Array.isArray(answer)) return answer.includes(optionLabel);
      return answer === optionLabel;
    },
    [formAnswers, currentKey],
  );

  const handleOptionSelect = useCallback(
    (optionLabel: string) => {
      if (answered) return;
      const key = `question_${currentIndex}`;
      const isMultiSelect = currentQuestion?.multiSelect ?? false;

      if (isMultiSelect) {
        const current = (formAnswers[key] as string[] | undefined) ?? [];
        if (optionLabel === OTHER_VALUE) {
          if (current.includes(OTHER_VALUE)) {
            setFormAnswers({ ...formAnswers, [key]: current.filter((o) => o !== OTHER_VALUE) });
          } else {
            setFormAnswers({ ...formAnswers, [key]: [OTHER_VALUE] });
          }
        } else {
          const filtered = current.filter((o) => o !== OTHER_VALUE);
          if (filtered.includes(optionLabel)) {
            setFormAnswers({ ...formAnswers, [key]: filtered.filter((o) => o !== optionLabel) });
          } else {
            setFormAnswers({ ...formAnswers, [key]: [...filtered, optionLabel] });
          }
        }
      } else {
        setFormAnswers({ ...formAnswers, [key]: optionLabel });
        if (optionLabel !== OTHER_VALUE) {
          setOtherInputs({ ...otherInputs, [key]: "" });
          // Auto-advance to next question after 150ms
          if (currentIndex < totalQuestions - 1) {
            setTimeout(() => setCurrentIndex((prev) => prev + 1), 150);
          }
        }
      }
    },
    [answered, currentIndex, currentQuestion?.multiSelect, formAnswers, otherInputs, totalQuestions],
  );

  const handleOtherInputChange = useCallback(
    (value: string) => {
      setOtherInputs({ ...otherInputs, [currentKey]: value });
    },
    [otherInputs, currentKey],
  );

  const handleSubmit = useCallback(() => {
    const answers: Record<string, string> = {};
    questions.forEach((_, qIndex) => {
      const key = `question_${qIndex}`;
      const selectedAnswer = formAnswers[key];
      const otherInput = otherInputs[key]?.trim();
      const q = questions[qIndex];
      const isMultiSelect = q.multiSelect ?? false;

      if (isMultiSelect) {
        const selected = Array.isArray(selectedAnswer) ? selectedAnswer : [];
        const values: string[] = [];
        for (const v of selected) {
          if (v === OTHER_VALUE) {
            if (otherInput) values.push(otherInput);
          } else {
            values.push(v);
          }
        }
        if (values.length > 0) {
          answers[q.question] = values.join(", ");
        }
      } else {
        if (selectedAnswer === OTHER_VALUE && otherInput) {
          answers[q.question] = otherInput;
        } else if (selectedAnswer && selectedAnswer !== OTHER_VALUE) {
          answers[q.question] = selectedAnswer as string;
        }
      }
    });
    onAnswer(answers);
  }, [questions, formAnswers, otherInputs, onAnswer]);

  const goToPrevious = useCallback(() => {
    setCurrentIndex((prev) => (prev > 0 ? prev - 1 : prev));
  }, []);

  const goToNext = useCallback(() => {
    setCurrentIndex((prev) => (prev < totalQuestions - 1 ? prev + 1 : prev));
  }, [totalQuestions]);

  // ---- Answered state: show Q&A summary ----
  if (answered) {
    return (
      <div className="border border-gray-200 rounded-xl bg-gray-50/50 p-4 my-3 space-y-2">
        <div className="flex items-center gap-2 mb-2">
          <HelpCircle className="h-3.5 w-3.5 text-gray-400" />
          <span className="text-xs font-medium text-gray-500">
            Answered {totalQuestions} question{totalQuestions !== 1 ? "s" : ""}
          </span>
        </div>
        {questions.map((q, qIndex) => {
          const key = `question_${qIndex}`;
          const answer = formAnswers[key];
          const otherInput = otherInputs[key]?.trim();
          let displayAnswer = "";
          if (Array.isArray(answer)) {
            const values = answer.map((v) => (v === OTHER_VALUE ? otherInput || "Other" : v));
            displayAnswer = values.join(", ");
          } else if (answer === OTHER_VALUE) {
            displayAnswer = otherInput || "Other";
          } else if (answer) {
            displayAnswer = answer;
          }
          return (
            <div key={qIndex} className="space-y-0.5">
              <p className="text-xs text-gray-500">{q.question}</p>
              <p className="text-xs font-medium text-gray-700">{displayAnswer}</p>
            </div>
          );
        })}
      </div>
    );
  }

  // ---- Active question card ----
  if (!currentQuestion) return null;

  const optionsCount = currentQuestion.options?.length ?? 0;
  const otherLetter = LETTER_OPTIONS[optionsCount] || String(optionsCount + 1);

  return (
    <div className="border-2 border-blue-200 rounded-xl bg-blue-50/50 my-3 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-blue-200 px-3 py-2">
        <div className="flex items-center gap-2">
          <div className="rounded-md bg-blue-100 p-1">
            <HelpCircle className="h-3.5 w-3.5 text-blue-600" />
          </div>
          <span className="text-xs font-medium text-blue-800">Questions</span>
        </div>
        {totalQuestions > 1 && (
          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={goToPrevious}
              disabled={currentIndex === 0}
              className="rounded p-0.5 text-gray-400 transition-colors hover:bg-gray-100 hover:text-gray-600 disabled:opacity-30 cursor-pointer"
              aria-label="Previous question"
            >
              <ChevronUp className="h-4 w-4" />
            </button>
            <span className="min-w-[3rem] text-center text-xs text-gray-500">
              {currentIndex + 1} of {totalQuestions}
            </span>
            <button
              type="button"
              onClick={goToNext}
              disabled={currentIndex === totalQuestions - 1}
              className="rounded p-0.5 text-gray-400 transition-colors hover:bg-gray-100 hover:text-gray-600 disabled:opacity-30 cursor-pointer"
              aria-label="Next question"
            >
              <ChevronDown className="h-4 w-4" />
            </button>
          </div>
        )}
      </div>

      {/* Question body */}
      <div className="p-3">
        <div className="mb-3 flex items-start gap-2">
          <span className="text-xs font-medium text-gray-600">
            {currentIndex + 1}.
          </span>
          <div>
            {currentQuestion.header && (
              <span className="text-xs font-semibold uppercase tracking-wider text-blue-600 bg-blue-100 px-2 py-0.5 rounded mr-2">
                {currentQuestion.header}
              </span>
            )}
            <p className="text-xs font-medium text-gray-800 mt-1">
              {currentQuestion.question}
            </p>
            {currentQuestion.multiSelect && (
              <span className="mt-1 inline-block rounded bg-gray-100 px-1.5 py-0.5 text-[10px] font-medium text-gray-500">
                Select multiple
              </span>
            )}
          </div>
        </div>

        {/* Options */}
        {currentQuestion.options && currentQuestion.options.length > 0 && (
          <div className="space-y-1">
            {currentQuestion.options.map((option, oIndex) => {
              const letter = LETTER_OPTIONS[oIndex] || String(oIndex + 1);
              const selected = isSelected(option.label);
              return (
                <button
                  key={oIndex}
                  type="button"
                  onClick={() => handleOptionSelect(option.label)}
                  className={`group flex w-full items-start gap-2.5 rounded-md px-2.5 py-1.5 text-left transition-colors cursor-pointer ${
                    selected
                      ? "bg-blue-100"
                      : "hover:bg-gray-100"
                  }`}
                >
                  <span
                    className={`flex h-5 w-5 flex-shrink-0 items-center justify-center rounded text-xs font-medium ${
                      selected
                        ? "bg-blue-600 text-white"
                        : "bg-gray-200 text-gray-500"
                    }`}
                  >
                    {letter}
                  </span>
                  <div className="min-w-0 flex-1">
                    <p
                      className={`text-xs transition-colors ${
                        selected
                          ? "font-medium text-gray-800"
                          : "text-gray-600"
                      }`}
                    >
                      {option.label}
                    </p>
                    {option.description && (
                      <p className="mt-0.5 text-[10px] text-gray-400">
                        {option.description}
                      </p>
                    )}
                  </div>
                </button>
              );
            })}

            {/* Other option */}
            {isOtherSelected ? (
              <div className="flex w-full items-center gap-2.5 rounded-md bg-blue-100 px-2.5 py-1.5">
                <button
                  type="button"
                  onClick={() => handleOptionSelect(OTHER_VALUE)}
                  className="flex-shrink-0 cursor-pointer"
                >
                  <span className="flex h-5 w-5 items-center justify-center rounded bg-blue-600 text-xs font-medium text-white">
                    {otherLetter}
                  </span>
                </button>
                <input
                  type="text"
                  placeholder="Type your answer..."
                  value={otherInputs[currentKey] ?? ""}
                  onChange={(e) => handleOtherInputChange(e.target.value)}
                  className="min-w-0 flex-1 bg-transparent text-xs text-gray-800 placeholder-gray-400 outline-none"
                  autoFocus
                />
              </div>
            ) : (
              <button
                type="button"
                onClick={() => handleOptionSelect(OTHER_VALUE)}
                className="group flex w-full items-center gap-2.5 rounded-md px-2.5 py-1.5 text-left transition-colors hover:bg-gray-100 cursor-pointer"
              >
                <span className="flex h-5 w-5 flex-shrink-0 items-center justify-center rounded bg-gray-200 text-xs font-medium text-gray-500">
                  {otherLetter}
                </span>
                <span className="text-xs text-gray-500">Other</span>
              </button>
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="flex items-center justify-end border-t border-blue-200 px-3 py-2">
        <button
          type="button"
          onClick={handleSubmit}
          disabled={!allQuestionsAnswered}
          className="px-4 py-1.5 text-xs font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors cursor-pointer"
        >
          Submit
        </button>
      </div>
    </div>
  );
}
