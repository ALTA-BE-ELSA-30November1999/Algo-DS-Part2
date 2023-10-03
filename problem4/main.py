def count_item_and_sort(items):
    List = {}
    for i in items:
        if i in List:
            List[i]  += 1
        else:
            List[i]= 1

    if List[i] == 1 :
        sorted_items = sorted(List.items())
        # print(sorted_items)
        return ' '.join([f"{item}->{count}" for item,count in sorted_items])

    else : 
        sorted_items = sorted(List.items(), key=lambda x: x[1])
        output = ""
        for item, count in sorted_items:
            output += f"{item}->{count}"
        return ' '.join([f"{item}->{count}" for item,count in sorted_items])   
    
if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"