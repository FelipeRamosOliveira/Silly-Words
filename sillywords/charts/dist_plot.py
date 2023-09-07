import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def WordDistPlot(dist_df, x='word', y='frequency', rank=20, palette='Greens_r'):
    sns.set(rc={'figure.figsize': (15, 5)})
    sns.set_style("white")
    ax = sns.barplot(x=x, y=y, palette=palette, data=dist_df.head(rank))
    plt.xticks(rotation=90)
    sns.despine(bottom = False, left = False)
    ax = ax
    return ax
