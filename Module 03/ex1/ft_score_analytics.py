import sys


def score_analytics():
    """Process and analyze player scores from command line"""
    print("=== Player Score Analytics ===")

    # Check if scores were provided
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py \
              <score1> <score2> ..."
        )
        return

    # Try to convert arguments to integers
    scores = []
    try:
        for arg in sys.argv[1:]:
            scores.append(int(arg))
    except ValueError:
        print("Error: Invalid score value. All scores must be integers.")
        return

    # Calculate statistics
    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    # Display results
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    score_analytics()
