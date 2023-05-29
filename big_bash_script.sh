for file in '#filepath' #filename *; do
    $(#filepath --input_path="$file") &
done
