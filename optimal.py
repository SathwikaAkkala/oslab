def optimal_page_replacement(pages, frame_size):
    page_frame = []
    page_faults = 0
    hits = 0

    for i in range(len(pages)):
        if pages[i] not in page_frame:
            page_faults += 1  # Count as a page fault
            if len(page_frame) < frame_size:
                page_frame.append(pages[i])  # Add the new page
            else:
                # Find the page to replace
                farthest = -1
                index_to_replace = -1
                for j in range(len(page_frame)):
                    try:
                        next_use = pages[i + 1:].index(page_frame[j])
                    except ValueError:
                        next_use = float('inf')  # This page is not used in the future
                    if next_use > farthest:
                        farthest = next_use
                        index_to_replace = j
                page_frame[index_to_replace] = pages[i]  # Replace the page
        else:
            hits += 1  # Count as a hit if the page is already in frame

    total_references = len(pages)
    miss_ratio = page_faults / total_references
    hit_ratio = hits / total_references

    return page_faults, hits, miss_ratio, hit_ratio

# Dynamic Input
pages_input = input("Enter the page reference string (comma-separated): ")
pages = list(map(int, pages_input.split(',')))
frame_size = int(input("Enter the frame size: "))

page_faults, hits, miss_ratio, hit_ratio = optimal_page_replacement(pages, frame_size)

print("Optimal Page Faults:", page_faults)
print("Hits:", hits)
print("Miss Ratio:", miss_ratio)
print("Hit Ratio:", hit_ratio)
