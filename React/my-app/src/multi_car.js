import React, { Component } from "react";

class MultiCar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cars: {
                selectedBrand: 'Toyota',
                selectedModel: 'Camry',
                selectedColor: 'red'
            },
            carBrands: {
                Toyota: ['Camry', 'Corolla', 'Rav4'],
                Audi: ['A4', 'A6', 'A8'],
                Lexus: ['RX', 'ES', 'GX'],
                Porsche: ['911', 'Cayenne', 'Panamera'],
                Mercedes: ['C-Class', 'E-Class', 'S-Class'],
            }
        }
    }

    changeBrand = (brand) => {
        this.setState((prevState) => ({
            cars: {
                ...prevState.cars,
                selectedBrand: brand,
                // Cập nhật model mặc định khi đổi hãng xe
                selectedModel: prevState.carBrands[brand][0],
            },
        }));
    };

    changeModel = (model) => {
        this.setState((prevState) => ({
            cars: {
                ...prevState.cars,
                selectedModel: model,
            },
        }));
    };

    // Sửa lại hàm để toggle màu giữa đỏ và xanh
    changeColor = () => {
        this.setState((prevState) => ({
            cars: {
                ...prevState.cars,
                selectedColor: prevState.cars.selectedColor === "red" ? "blue" : "red",
            },
        }));
    };

    render() {
        const { selectedBrand, selectedModel, selectedColor } = this.state.cars;
        const { carBrands } = this.state;
        const models = carBrands[selectedBrand] || [];
        return (
            <div className="car-container">
                <h1>Thong tin xe</h1>
                <div className="brand-selector">
                    <h3>Chon thuong hieu xe:</h3>
                    <div className="brand-buttons">
                    {Object.keys(carBrands).map((brand) => (
                        <button 
                        key={brand}
                        onClick={() => this.changeBrand(brand)}
                        className= {brand === selectedBrand ? 'active' : ''} >{brand}
                        </button>
                    ))}
                    </div>
                </div>
                <div className="model-selector">
                    <h3>Chon mau xe </h3>
                    <div className="model-buttons">
                        {models.map((model) => (
                            <button 
                            key={model}
                            onClick={() => this.changeModel(model)}
                            className={model === selectedModel ? 'active' : ''} >{model}
                            </button>
                        ))}
                    </div>
                </div>
                <div className="car-info">
                    <p>Thuong hieu: {selectedBrand}</p>
                    <p>Model: {selectedModel}</p>
                    <p>Mau sac: {selectedColor}</p>
                    <div className="car-display" style={{ backgroundColor: selectedColor }}>
                        <span>Xe màu {selectedColor}</span>
                    </div>
                    <button onClick={this.changeColor}>Doi mau</button>
                </div>
            </div>
        );
    }
}

export default MultiCar;