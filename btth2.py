import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
    "P04-Sạc Dự Phòng-300000",       
    "P05-Cáp Sạc Nhanh-150000VND-4.2" 
]

def parse_product(prod_str):
    try:
        parts = prod_str.split('-')
        if len(parts) < 4:
            print(f"Bỏ qua sản phẩm do sai cấu trúc dữ liệu: '{prod_str}'")
            return None
            
        id_sp, name, price_str, rating_str = parts[0], parts[1], parts[2], parts[3]
        price = int(price_str)
        rating = float(rating_str)
        return {"id": id_sp, "name": name, "price": price, "rating": rating}
    except ValueError:
        tmp_id = prod_str.split('-')[0] if '-' in prod_str else "Không rõ"
        print(f"Bỏ qua sản phẩm [{tmp_id}] do lỗi định dạng số")
        return None

def display_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    has_data = False
    for prod_str in product_list:
        prod_data = parse_product(prod_str)
        if not prod_data:
            continue
            
        has_data = True
        formatted_price = f"{prod_data['price']:,} VND"
        label_map = {
            "id": f"{prod_data['id']:<10}",
            "name": prod_data['name'],
            "price": formatted_price,
            "rating": prod_data['rating']
        }
        template = "Mã: {id} | Tên: {name:<20} | Giá: {price:<16} | Rating: {rating}*"
        print(template.format_map(label_map))
        
    if not has_data:
        print("Không có sản phẩm nào hợp lệ để in tem nhãn.")

def sort_products_smart():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    global product_list
    valid_products = []
    invalid_products = []
    
    for prod in product_list:
        if parse_product(prod) is not None:
            valid_products.append(prod)
        else:
            invalid_products.append(prod)
            
    if not valid_products:
        print("Không có sản phẩm hợp lệ nào để sắp xếp!")
        return

    valid_products.sort(key=lambda x: (-parse_product(x)["rating"], parse_product(x)["price"]))
    product_list = valid_products + invalid_products
    
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for idx, prod in enumerate(valid_products, 1):
        print(f"{idx}. {prod}")

def calculate_total_inventory():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    prices = [parse_product(p)["price"] for p in product_list if parse_product(p) is not None]
    if not prices:
        print("Kho hàng trống hoặc không có dữ liệu giá tiền hợp lệ.")
        return
        
    total_value = functools.reduce(lambda acc, curr: acc + curr, prices)
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total_value:,} VND.")

def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce)")
        print("4. Đóng hệ thống")
        print("================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        if choice == '1':
            display_labels()
        elif choice == '2':
            sort_products_smart()
        elif choice == '3':
            calculate_total_inventory()
        elif choice == '4':
            print("Đang đóng hệ thống... Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 4.")
    main()