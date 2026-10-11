import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Excel Dataset

file_path = "Business_Data.xlsx"

df = pd.read_excel(file_path, header=2)

# Remove completely empty rows
df = df.dropna(how="all").copy()

# Remove rows without Business ID
df = df.dropna(subset=["Business_ID"]).copy()

print("\n========== DATASET LOADED ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Display First 5 Records

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())


# 3. Dataset Information

print("\n========== DATASET INFORMATION ==========")
print(df.info())

# 4. Column Names

print("\n========== COLUMN NAMES ==========")

for column in df.columns:
    print(column)

# 5. Missing Values

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

# 6. Duplicate Records

print("\n========== DUPLICATE RECORDS ==========")

duplicates = df.duplicated().sum()

print("Duplicate records:", duplicates)

# 7. City-wise Business Count

print("\n========== CITY-WISE BUSINESS COUNT ==========")

city_count = df["City"].value_counts()

print(city_count)


# Graph

plt.figure(figsize=(8, 5))

city_count.plot(kind="bar")

plt.title("Number of Businesses by City")
plt.xlabel("City")
plt.ylabel("Number of Businesses")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# 8. Industry-wise Business Count

print("\n========== INDUSTRY-WISE BUSINESS COUNT ==========")

industry_count = df["Industry"].value_counts()

print(industry_count)


plt.figure(figsize=(8, 5))

industry_count.plot(kind="bar")

plt.title("Businesses by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Businesses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 9. Business Type Analysis

print("\n========== BUSINESS TYPE ==========")

business_type = df["Business Type"].value_counts()

print(business_type)


plt.figure(figsize=(8, 5))

business_type.head(10).plot(kind="bar")

plt.title("Top Business Types")
plt.xlabel("Business Type")
plt.ylabel("Number of Businesses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 10. Online Presence Analysis

print("\n========== ONLINE PRESENCE ==========")

online_presence = df["Online Presence"].value_counts()

print(online_presence)


plt.figure(figsize=(7, 5))

online_presence.plot(kind="bar")

plt.title("Online Presence of Businesses")
plt.xlabel("Online Presence")
plt.ylabel("Number of Businesses")

plt.tight_layout()
plt.show()

# 11. Google Rating Analysis

print("\n========== GOOGLE RATING ==========")

df["Google Rating"] = pd.to_numeric(
    df["Google Rating"], errors="coerce"
)

print(df["Google Rating"].describe())


plt.figure(figsize=(8, 5))

plt.hist(
    df["Google Rating"].dropna(),
    bins=8
)

plt.title("Distribution of Google Ratings")
plt.xlabel("Google Rating")
plt.ylabel("Number of Businesses")

plt.tight_layout()
plt.show()

# 12. Website Availability

print("\n========== WEBSITE AVAILABILITY ==========")

website_count = df["Website"].value_counts()

print(website_count)

# Create Website Status

df["Website Status"] = df["Website"].apply(
    lambda x: "Available"
    if pd.notna(x) and str(x).lower() not in
    ["not found", "not available"]
    else "Not Available"
)

print("\nWebsite Status:")
print(df["Website Status"].value_counts())


plt.figure(figsize=(7, 5))

df["Website Status"].value_counts().plot(kind="bar")

plt.title("Website Availability")
plt.xlabel("Website Status")
plt.ylabel("Number of Businesses")

plt.tight_layout()
plt.show()

# 13. Problem Category Analysis

print("\n========== PROBLEM CATEGORY ==========")

problem_category = df["Problem Category"].value_counts()

print(problem_category)


plt.figure(figsize=(8, 5))

problem_category.plot(kind="bar")

plt.title("Business Problem Categories")
plt.xlabel("Problem Category")
plt.ylabel("Number of Businesses")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 14. Required Service Analysis

print("\n========== REQUIRED SERVICES ==========")

required_service = df["Required Service"].value_counts()

print(required_service.head(10))

# 15. Requirement Status

print("\n========== REQUIREMENT STATUS ==========")

requirement_status = df["Requirement Status"].value_counts()

print(requirement_status)


plt.figure(figsize=(8, 5))

requirement_status.plot(kind="bar")

plt.title("Requirement Status")
plt.xlabel("Requirement Status")
plt.ylabel("Number of Businesses")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 16. Urgency Analysis

print("\n========== URGENCY ==========")

urgency = df["Urgency"].value_counts()

print(urgency)


plt.figure(figsize=(7, 5))

urgency.plot(kind="bar")

plt.title("Business Requirement Urgency")
plt.xlabel("Urgency")
plt.ylabel("Number of Businesses")

plt.tight_layout()
plt.show()

# 17. Budget Status

print("\n========== BUDGET STATUS ==========")

budget = df["Budget Status"].value_counts()

print(budget)

# 18. Follow-Up Status

print("\n========== FOLLOW-UP STATUS ==========")

follow_up = df["Follow-Up Status"].value_counts()

print(follow_up)

# 19. Statistical Summary

print("\n========== STATISTICAL SUMMARY ==========")

print("\nGoogle Rating Statistical Summary:")
print(df["Google Rating"].describe())

# 20. Final EDA Summary

print("\n========================================")
print("        EDA COMPLETED SUCCESSFULLY")
print("========================================")

print("Total Businesses:", len(df))
print("Total Columns:", len(df.columns))
print("Duplicate Records:", df.duplicated().sum())

print("\nBusinesses by City:")
print(df["City"].value_counts())

print("\nTop Industries:")
print(df["Industry"].value_counts().head())

print("\nOnline Presence:")
print(df["Online Presence"].value_counts())

print("\nWebsite Status:")
print(df["Website Status"].value_counts())

print("\nRequirement Status:")
print(df["Requirement Status"].value_counts())
