# Split files
import splitfolders

input_folder = 'E:/Datasets/VATS/images_split/images_all'
output_folder = 'E:/Datasets/VATS/images_split/output_all_10'

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output=output_folder,
    seed=42, ratio=(.8, .1, .1), group_prefix=None, move=False) # default values
