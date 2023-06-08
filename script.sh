# loop through folders and subfolders and rename all files to random numbers

find . -type f -name '*.png' -print0 | while IFS= read -r -d '' file; do
    mv "$file" "$((RANDOM%2000+500)).png"
done
