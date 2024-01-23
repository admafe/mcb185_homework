gunzip -c dictionary.gz | grep -E "r" | grep -v "[^rzoniac]" | grep -E ".{4,}"
gunzip -c dictionary.gz | grep -E "r" | grep -v "[^rzoniac]" | grep -E ".{4,}" | wc -l