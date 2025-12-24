import React,{useState} from "react";

const Contact = () =>{
    const [formData, setFormData] = useState({
        email: '',
        message: '',
    });

    const [errors, setErrors] = useState({});
    const [submitted, setSubmitted] = useState(false);

    const handleInputChange = (e) =>{
        const {name, value} = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const validateForm = () => {
        const errors ={};
        if(!formData.email.trim()){
            errors.email = 'Email khong duoc de trong';
        }
        else if(!/\S+@\S+\.\S+/.test(formData.email)){
            errors.email = 'Email khong hop le';
        }
        if(!formData.message.trim()){
            errors.message = 'Tin nhan khong duoc de trong';
        }
        return errors;
    };

    const handleSubmit = (e) =>{
        e.preventDefault();
        const validationErrors= validateForm();
        if(Object.keys(validationErrors).length === 0){
            setSubmitted(true);
            setFormData({
                email: '',
                message: '',
            });
            setErrors({});
        }
        else{
            setErrors(validationErrors);
        }
    };

    return(
        <div className="contact">
            <h2>Lien he</h2>
            {submitted ? (
                <p>Cam on ban da gui thong tin! Chung toi se lien he som</p>
            ) : (
                <form onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="email">Email:</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleInputChange}
                        />
                        {errors.email && <p className="error">{errors.email}</p>}
                    </div>
                    <div>
                        <label>Noi dung:</label>
                        <textarea
                            id="message"
                            name="message"
                            value={formData.message}
                            onChange={handleInputChange}
                        ></textarea>
                        {errors.message && <p className="error">{errors.message}</p>}
                    </div>
                    <button type="submit">Gui thong tin</button>
                </form>
            )}
        </div>
    );
}

export default Contact;