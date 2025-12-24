import React, {Component} from "react";

class Car extends Component{
    constructor(props){
        super(props);
        this.state = {
            car: {
            brand: "Toyota",
            model: "Camry",
            color: "red",
            },
        };
    }
    changeColor = () => {
        this.setState(prevState => ({
            car: {
                ...prevState.car,
                color: prevState.car.color === "red" ? "blue" : "red",
            },
        }));
    }


    render(){
        const { brand, model, color } = this.state.car;
        return(
            <div className="car-container">
                <h1>Thong tin xe</h1>
                <p>Thuong hieu: {brand}</p>
                <p>Mau sac: {color}</p>
                <div className="car-display" style={{backgroundColor:color}}>
                    <span>Xe mau</span>
                </div>
                <button onClick={this.changeColor}>Doi mau</button>
            </div>
        )
    }
}

export default Car;