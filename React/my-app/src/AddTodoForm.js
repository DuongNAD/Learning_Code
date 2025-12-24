import React, { useState } from "react";

function AddTodoForm({onAddTodo}){

    const [text, setText] = useState('');

    const handleInputChange = (e)=>{
        setText(e.target.value);
    };

    const handleSubmit = (e)=>{
        e.preventDefault();

        if (text.trim()) {
            onAddTodo(text);
            setText('');
        }
        else{
            alert('Vui lòng nhập nội dung công việc');
        }
    };

    return(
        <form onSubmit={handleSubmit} style={{marginBottom:'20px'}}>
            <h3>Them cong viec</h3>
            <div>
                <input 
                    type="text"
                    value={text}
                    onChange={handleInputChange}
                    placeholder="Nhập nội dung công việc"
                    style={{ marginRight: '10px', padding: '5px', width: '300px' }}
                />
                <button type="submit" style={{padding:'5px 10px'}}>Thêm</button>
            </div>
        </form>
    );
}

export default AddTodoForm;