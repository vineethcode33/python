"""basic implementation of a binary search"""

def search_binary(search_list, search_element):
	
	search_list = sorted(search_list)
	print search_list
	first_pos = 0
	last_pos = len(search_list)-1
	
	found = False

	while first_pos < last_pos and not found:
		mid_pos = (first_pos + last_pos) / 2

		if search_list[mid_pos] == search_element:
			found = True

		else:
			if search_list[mid_pos] > search_element:
				last_pos = mid_pos -1
			else:
				first_pos = mid_pos +1

	return found


if __name__ == "__main__":
	print search_binary([7,2,5,9,10],3)