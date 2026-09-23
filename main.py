import geopandas as gpd 

bg = gpd.read_file("data/raw/tl_2025_48_bg.zip")

print(bg.shape)
print(bg.crs)
print(bg.columns.tolist())
print(bg.head())
