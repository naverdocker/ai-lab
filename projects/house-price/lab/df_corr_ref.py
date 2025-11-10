# ---------- CORRELATION EXPLORATION (minimal dependencies) ----------

print("\n---- correlations with target ----")
corr = df.corr(numeric_only=True)
target_corr = corr[TCOL].sort_values(ascending=False)
print(target_corr)

# 1) top positive and negative correlations
top_pos = target_corr.index[1]   # skip target itself
top_neg = target_corr.index[-1]
print(f"\nMost positively correlated with {TCOL}: {top_pos} ({target_corr[top_pos]:.3f})")
print(f"Most negatively correlated with {TCOL}: {top_neg} ({target_corr[top_neg]:.3f})")

# 2) full correlation heatmap (matplotlib only)
plt.figure(figsize=(8,6))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Correlation coefficient")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# 3) bar plot of correlations with target
plt.figure(figsize=(8,4))
plt.bar(target_corr.index, target_corr.values)
plt.xticks(rotation=90)
plt.ylabel("Correlation coefficient")
plt.title(f"Correlation of each feature with {TCOL}")
plt.tight_layout()
plt.show()

# 4) scatter plots for strongest positive and negative features
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(df[top_pos], df[TCOL], s=10, alpha=0.5)
plt.xlabel(top_pos); plt.ylabel(TCOL)
plt.title(f"{top_pos} vs {TCOL}")

plt.subplot(1,2,2)
plt.scatter(df[top_neg], df[TCOL], s=10, alpha=0.5)
plt.xlabel(top_neg); plt.ylabel(TCOL)
plt.title(f"{top_neg} vs {TCOL}")

plt.tight_layout()
plt.show()

# 5) optional: identify feature pairs with high inter-correlation
from itertools import combinations
print("\nHighly correlated feature pairs (|r| > 0.8):")
for a, b in combinations(corr.columns, 2):
    r = corr.loc[a, b]
    if abs(r) > 0.8 and a != b:
        print(f"{a:15s} {b:15s} {r:6.3f}")



###############
# CORR WITH SNS
###############
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))
sns.heatmap(corr, cmap="coolwarm", annot=False, center=0)
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.show()


##
target_corr = corr[TCOL].drop(TCOL).sort_values(ascending=False)
topn = target_corr.head(10)
plt.figure(figsize=(6,4))
sns.barplot(x=topn.values, y=topn.index)
plt.title(f"Top correlations with {TCOL}")
plt.xlabel("Correlation coefficient")
plt.tight_layout()
plt.show()


##
top_pos = target_corr.index[0]
top_neg = target_corr.index[-1]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(df[top_pos], df[TCOL], s=10, alpha=0.5)
plt.title(f"{top_pos} vs {TCOL}")
plt.subplot(1,2,2)
plt.scatter(df[top_neg], df[TCOL], s=10, alpha=0.5)
plt.title(f"{top_neg} vs {TCOL}")
plt.tight_layout()
plt.show()


##
from itertools import combinations

high_pairs = []
for a, b in combinations(df.columns, 2):
    r = corr.loc[a, b]
    if abs(r) > 0.8 and a != TCOL and b != TCOL:
        high_pairs.append((a, b, r))

print("\nHighly correlated feature pairs (|r| > 0.8):")
for a, b, r in high_pairs:
    print(f"{a:15s} {b:15s} {r:6.3f}")


##
spearman = df.corr(method="spearman", numeric_only=True)[TCOL].sort_values(ascending=False)
print("\nSpearman correlations:")
print(spearman)


##
from sklearn.feature_selection import mutual_info_regression

X = df.drop(columns=[TCOL]).select_dtypes("number")
y = df[TCOL]
mi = mutual_info_regression(X, y, random_state=42)
mi_series = pd.Series(mi, index=X.columns).sort_values(ascending=False)
print("\nMutual information with target:")
print(mi_series.head(10))


##
top_features = target_corr.abs().sort_values(ascending=False).head(8).index.tolist() + [TCOL]
sns.heatmap(df[top_features].corr(), annot=True, cmap="coolwarm", center=0)
plt.title("Top correlated features and their inter-correlation")
plt.show()

