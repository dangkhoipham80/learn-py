**database.py**:

install: sqlalchemy

create_engine: Dùng để tạo một "engine" – đối tượng trung gian để giao tiếp với cơ sở dữ liệu.
sessionmaker: Tạo một "Session" – đối tượng quản lý các phiên làm việc với cơ sở dữ liệu (giống như mở và đóng kết nối).
declarative_base: Dùng để tạo một lớp cơ sở, từ đó bạn sẽ định nghĩa các model (bảng) cho cơ sở dữ liệu

sqlite:///./todosapp.db:
sqlite:// là schema của SQLite.
./todosapp.db là đường dẫn tương đối đến file cơ sở dữ liệu (nằm trong thư mục hiện tại).

connect_args={'check_same_thread': False}: dành riêng cho SQLite.
SQLite mặc định không cho nhiều thread cùng truy cập cùng một connection. Tham số này tắt cơ chế đó (cho phép nhiều thread cùng sử dụng)

Tạo SessionLocal – class quản lý phiên làm việc với DB
autocommit=False: Bạn phải tự commit thay đổi (an toàn hơn).
autoflush=False: Không tự động ghi thay đổi về cơ sở dữ liệu khi truy vấn.
bind=engine: Gắn engine đã tạo ở trên vào SessionLocal.

Tạo lớp cơ sở cho các mô hình ORM
Base = declarative_base()
Base là lớp cơ sở từ declarative_base() của SQLAlchemy.
-> Khi bạn định nghĩa model như User, Todo,... thì bạn sẽ kế thừa từ Base.
