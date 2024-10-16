document.addEventListener("DOMContentLoaded", function() {
    // 获取所有删除按钮
    const deleteButtons = document.querySelectorAll("#deleteWordBtn");

    deleteButtons.forEach(button => {
        // 为每个删除按钮添加点击事件
        button.addEventListener("click", function() {
            const wordId = this.closest('tr').querySelector('th').innerText;  // 获取当前行的ID

            // 确认是否删除
            if (confirm("确定要删除这个敏感词吗？")) {
                // 发送 DELETE 请求
                fetch(`delete/${wordId}`, {
                    method: 'DELETE',
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "success") {
                        // 删除成功后，从页面中移除该行
                        alert(data.message);
                        this.closest('tr').remove();  // 删除表格行
                    } else {
                        alert(data.message);  // 显示错误信息
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('删除请求失败，请重试。');
                });
            }
        });
    });
});