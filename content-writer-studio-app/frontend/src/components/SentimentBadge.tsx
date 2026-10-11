// ---------------------------------------------------------------------------
// Name:     Rahul Singh Bana
// Email:    bana.saa@gmail.com
// LinkedIn: https://www.linkedin.com/in/rahulsinghbana
// Repo:     https://github.com/rahulbana/rahulbana
// ---------------------------------------------------------------------------
import { Badge } from "@mantine/core";

const COLORS: Record<string, string> = {
  positive: "teal",
  negative: "red",
  neutral: "gray",
};

export function SentimentBadge({ sentiment }: { sentiment: string }) {
  const key = (sentiment || "neutral").toLowerCase();
  return (
    <Badge color={COLORS[key] ?? "gray"} variant="light" tt="capitalize">
      {sentiment || "neutral"}
    </Badge>
  );
}
