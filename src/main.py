import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def dataset_import(file_path=None):
    if file_path is None:
        base_path = os.getcwd()  # Get current working directory
        file_path = os.path.join(base_path, "polling_place_20240514.csv")
    df_raw = pl.read_csv(
        file_path,
        infer_schema_length=0,
        has_header=True,
        sep='\t',  # Use the correct parameter name
        encoding='utf-16',  # Adjust based on actual file encoding
        ignore_errors=True,  # Skip over problematic rows
    )
    return df_raw



def data_modeling(df_raw):
    # Drop rows with null values in critical columns
    df_edited = df_raw.drop_nulls(subset=["polling_place_id", "polling_place_name"])

    # Convert data types if necessary
    df_edited = df_edited.with_columns(
        [
            pl.col("polling_place_id").cast(pl.Int32),
            pl.col("zip").cast(pl.Int32),
            pl.col("election_dt").str.strptime(pl.Date, "%m/%d/%Y"),
        ]
    )

    return df_edited


def calculate_polling_places_per_county(df):
    return df.groupby("county_name").agg(
        pl.count("polling_place_id").alias("num_polling_places")
    )


def calculate_mean_polling_places(df_counts):
    return df_counts["num_polling_places"].mean()


def calculate_median_polling_places(df_counts):
    return df_counts["num_polling_places"].median()


def calculate_std_polling_places(df_counts):
    return df_counts["num_polling_places"].std()


def plot_polling_places_per_county(df, save_directory):
    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Calculate the number of polling places per county
    df_counts = df.groupby("county_name").agg(
        pl.count("polling_place_id").alias("num_polling_places")
    )

    # Convert to pandas DataFrame for plotting
    df_counts_pd = df_counts.to_pandas()

    # Plot
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df_counts_pd,
        x="county_name",
        y="num_polling_places",
        palette="Spectral"
    )
    plt.title("Number of Polling Places per County")
    plt.xlabel("County Name")
    plt.ylabel("Number of Polling Places")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig(os.path.join(save_directory, "polling_places_per_county.png"))
    plt.close()

def generate_markdown_report(df_counts, mean_polling_places, median_polling_places, std_polling_places, save_directory="."):
    """生成一个Markdown报告，包含描述性统计和可视化的结果"""
    
    # Markdown 文件路径
    md_file_path = os.path.join(save_directory, 'polling_places_analysis_report.md')
    
    with open(md_file_path, 'w') as f:
        f.write('# Polling Places Analysis Report\n\n')
        
        # 添加统计结果
        f.write('## Descriptive Statistics\n\n')
        f.write(f'**Mean Number of Polling Places per County:** {mean_polling_places:.2f}\n\n')
        f.write(f'**Median Number of Polling Places per County:** {median_polling_places}\n\n')
        f.write(f'**Standard Deviation of Polling Places per County:** {std_polling_places:.2f}\n\n')
        
        # 解释性的文本
        f.write('This section provides the summary statistics of polling places across different counties. '
                'The mean, median, and standard deviation help in understanding the distribution of polling places.\n\n')
        
        # 添加可视化结果
        f.write('## Visualizations\n\n')
        f.write('### Polling Places per County\n\n')
        f.write('![Number of Polling Places per County](polling_places_per_county.png)\n\n')
        
        # 总结
        f.write('## Conclusion\n\n')
        f.write('From the analysis, we observe the distribution of polling places across counties. '
                'Further analysis could include comparing these numbers with voter population data to ensure accessibility.\n')
    
    print(f"Markdown report generated at: {md_file_path}")


def main():
    # Load the dataset
    df_raw = dataset_import()

    # Model the data
    df_edited = data_modeling(df_raw)

    # Calculate statistics
    df_counts = calculate_polling_places_per_county(df_edited)
    mean_polling_places = calculate_mean_polling_places(df_counts)
    median_polling_places = calculate_median_polling_places(df_counts)
    std_polling_places = calculate_std_polling_places(df_counts)

    # Print calculated statistics
    print(f"Polling Places per County:\n{df_counts}\n")
    print(f"Mean Number of Polling Places per County: {mean_polling_places:.2f}")
    print(f"Median Number of Polling Places per County: {median_polling_places}")
    print(f"Standard Deviation: {std_polling_places:.2f}")

    # Define the save directory for plots
    save_directory = "."

    # Plot the data
    plot_polling_places_per_county(df_edited, save_directory)

    generate_markdown_report(df_counts, mean_polling_places, median_polling_places, std_polling_places, save_directory)


if __name__ == "__main__":
    main()
