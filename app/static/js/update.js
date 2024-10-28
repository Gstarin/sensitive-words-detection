function openUpdateModal(id, word, regex, type) {
    // 填充表单字段
    document.getElementById('update-word-id').value = id;
    document.getElementById('update-word').value = word;
    document.getElementById('update-regex').value = regex;
    document.getElementById('update-type').value = type;
    console.log(id,type);
    
    // 显示模态框
    let updateModal = new bootstrap.Modal(document.getElementById('updateWordModal'));
    updateModal.show();
}

function submitUpdateForm(event) {
    event.preventDefault();  // 阻止表单默认提交行为

    const id = document.getElementById('update-word-id').value;
    const word = document.getElementById('update-word').value;
    const existingRegex = document.getElementById('update-regex').value;

    // 获取被选中的单选按钮的值
    const type = document.querySelector('input[name="type"]:checked').value;

    console.log(word);
    console.log(type);


    // 将两个新正则表达式添加到现有的 regex 中
    const updatedRegex = existingRegex;

    // 构建要发送的数据
    const formData = {
        word: word,
        regex: updatedRegex,
        type: type  // 这里是用户选择的 type 值
    };

    // 使用 fetch 提交表单数据
    fetch(`update/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrf_token]').value // 如果你在使用 CSRF 保护
        },
        body: JSON.stringify(formData)  // 将数据序列化为 JSON 字符串
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('更新成功！');
            location.reload();  // 刷新页面或你可以选择其他方式更新表格
        } else {
            alert('更新失败：' + data.message);
        }
    })
    .catch(error => {
        console.error('错误:', error);
    });
}
