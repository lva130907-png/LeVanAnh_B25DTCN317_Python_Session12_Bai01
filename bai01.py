cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
    	"id": "P002",
    	"name": "Op lung Silicon", 
    	"number": 2, 
    	"price": 150000
    }
]

while True:
    print(""" 
==============================================
        SHOPPE CART MANAGEMENT SYSTEM
==============================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mời / Cộng dồn số lượng
3. Cập nhật số lượng của 1 sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
==============================================
 """)
    choose = input("Mời bạn chọn lựa chức năng (1-5): ")
    if choose == "1":
        print("--- CHI TIẾT GIỎ HÀNG ---")
        print(f'{"STT":<3} | {"Mã SP":<7} | {"Tên Sản Phẩm":<22} | {"SL":<3} | {"Đơn Giá":<11}  | {"Thành tiền":<11}')
        count = 0
        total = 0
        if cart_items == []:
            print("\n                           DANH SÁCH RỖNG!!!\n")
        else:
            for index, cart in enumerate(cart_items):
                total_price = cart["number"] * cart["price"]
                count += cart["number"]
                total += total_price
                print(f"{index+1:<3} | {cart['id']:<7} | {cart['name']:<22} | {cart['number']:<3} | {cart['price']:<11,}đ | {total_price:<11,}đ")

        print("------------------------------------------------------------------------------")

        print(f"=> Tổng số lượng sản phẩm trong giỏ: {count}")
        print(f"=> TỔNG TIỀN THANH TOÁN: {total:,}đ")

    elif choose == "2":
        add_cart = input("Nhập mã sản phẩm: ").strip().upper()
        flag = False
        for cart in cart_items:
            if cart["id"] == add_cart:
                print("Hệ Thống xác nhận đã có mã đơn hàng này! Tự động cộng dồn số lượng mới nhập vào số lượng cũ!")
                flag = True

                while True:
                    quantity_cart = input("Nhập số lượng sản phẩm: ")
                    if not quantity_cart.isdigit() or int(quantity_cart) <= 0:
                        print("Số lượng không hợp lệ, xin vui lòng nhập lại!")
                    else:
                        break
                quantity_cart = int(quantity_cart)
                cart["number"] += quantity_cart
                print("Cộng dồn thành công!!!")
                break

        if flag == False:
            name_cart = input("Nhập tên sản phẩm: ").strip()
            while True:
                    quantity_cart = input("Nhập số lượng sản phẩm: ")
                    if not quantity_cart.isdigit() or int(quantity_cart) <= 0:
                        print("Số lượng không hợp lệ, xin vui lòng nhập lại!")
                    else:
                        break

            quantity_cart = int(quantity_cart)

            while True:
                price_cart = input("Nhập đơn giá: ")
                if not price_cart.isdigit() or int(price_cart) <= 0:
                    print("Đơn giá không hợp lệ. Xin vui lòng nhập lại!")
                else:
                    break
            
            price_cart = int(price_cart)
            
            new_cart = {
                "id": add_cart,
                "name": name_cart, 
                "number": quantity_cart,
                "price": price_cart
            }

            cart_items.append(new_cart)
            print("Thêm thành công đơn hàng mới!")
    
    elif choose == "3":
        update_id = input("Nhập mã sản phẩm cần cập nhật số lượng: ").strip().upper()
        flag = False
        for cart in cart_items:
            if cart["id"] == update_id:
                flag = True
                while True:
                    update_quantity = input("Nhập số lượng mới: ")
                    if not update_quantity.isdigit() or int(update_quantity) <= 0:
                        print("Số lượng mới không hợp lệ. Xin vui lòng nhập lại!")
                    else:
                        update_quantity = int(update_quantity)
                        cart["number"] = update_quantity
                        print("Cập nhật thành công!")
                        break
                break
        if flag == False:
            print("Không tìm thấy sản phẩm")
    elif choose == "4":
        remove_id = input("Nhập mã sản phẩm bạn muốn xóa: ").strip().upper()
        flag = False
        for cart in cart_items:
            if cart["id"] == remove_id:
                flag = True
                cart_items.remove(cart)
                print("Đã xóa thành công!")
                break
        
        if flag == False:
            print("Không tìm thấy mã cần xóa!")

    elif choose == "5":
        print("Thoát chương trình...")
        break
    else:
        print("Lựa chọn không hợp lệ. Xin vui lòng nhập lại!")