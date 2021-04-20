# Naive Bayes-based article classifier

<h4>Dữ liệu</h4>
<p>Train: 48 bài báo lấy từ Vietnamnet thuộc 3 thể loại "Chính trị", "Thể thao", "Giáo dục"</p>
<p>Test: 9 bài báo lấy từ các trang báo khác (Tuổi trẻ, Nhân dân, VnExpress, giaoduc.net.vn)</p>
<h4>Tokenizer</h4>
<p>CocCoc tookenizer (https://github.com/coccoc/coccoc-tokenizer)</p>
<h4>Smoothing</h4>
<p>Tăng tử số lên 1 và mẫu số lên 2</p>
<h4>Tính toán</h4>
<p>Chuyển từ tính tích sang tính tổng log để tránh số lớn</p>
