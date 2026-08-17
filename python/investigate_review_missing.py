import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"

reviews = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_reviews_dataset.csv")
)

print("=" * 70)
print("INVESTIGATION OF REVIEW MISSING VALUES")
print("=" * 70)


# --------------------------------------------------
# 1. Review score distribution
# --------------------------------------------------

print("\n1. REVIEW SCORE DISTRIBUTION")
print("-" * 70)

print(
    reviews["review_score"].value_counts().sort_index()
)


# --------------------------------------------------
# 2. Reviews with and without comments
# --------------------------------------------------

print("\n2. COMMENT AVAILABILITY")
print("-" * 70)

has_title = reviews["review_comment_title"].notna()
has_message = reviews["review_comment_message"].notna()

print("Reviews with title:", has_title.sum())
print("Reviews without title:", (~has_title).sum())

print("Reviews with message:", has_message.sum())
print("Reviews without message:", (~has_message).sum())


# --------------------------------------------------
# 3. Missing comments by review score
# --------------------------------------------------

print("\n3. MISSING COMMENTS BY REVIEW SCORE")
print("-" * 70)

comment_analysis = (
    reviews
    .groupby("review_score")
    .agg(
        total_reviews=("review_id", "count"),
        missing_title=("review_comment_title", lambda x: x.isna().sum()),
        missing_message=("review_comment_message", lambda x: x.isna().sum())
    )
)

comment_analysis["missing_title_%"] = (
    comment_analysis["missing_title"]
    / comment_analysis["total_reviews"] * 100
).round(2)

comment_analysis["missing_message_%"] = (
    comment_analysis["missing_message"]
    / comment_analysis["total_reviews"] * 100
).round(2)

print(comment_analysis)


# --------------------------------------------------
# 4. Review score completeness
# --------------------------------------------------

print("\n4. REVIEW SCORE MISSING VALUES")
print("-" * 70)

print(
    "Missing review scores:",
    reviews["review_score"].isna().sum()
)


# --------------------------------------------------
# 5. Review records with no comments at all
# --------------------------------------------------

print("\n5. REVIEWS WITHOUT ANY COMMENT")
print("-" * 70)

no_comments = reviews[
    reviews["review_comment_title"].isna()
    &
    reviews["review_comment_message"].isna()
]

print(
    "Reviews without title AND message:",
    len(no_comments)
)

print(
    "Percentage:",
    f"{len(no_comments) / len(reviews) * 100:.2f}%"
)


print("\n" + "=" * 70)
print("REVIEW MISSING-VALUE INVESTIGATION COMPLETED")
print("=" * 70)
