import React, { Component } from "react";
import './App.css';

class CarSearchApp extends Component {
    constructor(props) {
        super(props);
        this.state = {
            carBrands: {
                Toyota: ['Camry', 'Corolla', 'Rav4'],
                Audi: ['A4', 'A6', 'A8'],
                Lexus: ['RX', 'ES', 'GX'],
                Porsche: ['911', 'Cayenne', 'Panamera'],
                Mercedes: ['C-Class', 'E-Class', 'S-Class'],
            },
            searchQuery: '',
            searchError: '',
            cars: {
                selectedBrand: '',
                selectedModel: '',
                selectedColor: 'red',
                availableModels: [],
            },
        };

    }

    handleInputChange = (e) => {
        this.setState({ searchQuery: e.target.value });
    };

    handleSearch = () => {
        const { searchQuery, carBrands } = this.state;
        const brandFound = Object.keys(carBrands).find(brand => brand.toLowerCase() === searchQuery.toLowerCase().trim());

        if (brandFound) {
            const modelsOfBrand = carBrands[brandFound];
            this.setState({
                cars: {
                    ...this.state.cars,
                    selectedBrand: brandFound,
                    availableModels: modelsOfBrand,
                    selectedModel: modelsOfBrand[0],
                },
                searchError: '',
                searchQuery: ''
            });
        } else {
            this.setState({
                searchError: `Khong tim thay hang xe "${searchQuery}"`,
                cars: {
                    selectedBrand: '',
                    selectedModel: '',
                    selectedColor: 'red',
                    availableModels: [],
                },
            });
        }
    };

    changeModel = (e) => {
        this.setState(prevState => ({
            cars: {
                ...prevState.cars,
                selectedModel: e.target.value,
            },
        }));
    };

    changeColor = (e) => {
        this.setState(prevState => ({
            cars: {
                ...prevState.cars,
                selectedColor: prevState.cars.selectedColor === "red" ? "blue" : "red",
            },
        }));
    }

    render() {
        const { searchQuery, searchError, cars } = this.state;
        return (
            <div className="container">
                <h1>Tim kiem xe</h1>
                <div className="search-section">
                    <input
                        type="text"
                        placeholder="Nhap ten hang xe"
                        value={searchQuery}
                        onChange={this.handleInputChange}
                    />
                    <button onClick={this.handleSearch}>Tim kiem</button>
                </div>

                {searchError && <p className="error-message">{searchError}</p>}

                {cars.selectedBrand && (
                    <div className="result-section">
                        <h2>Ket qua tim kiem cho: {cars.selectedBrand}</h2>
                        <div className="control-group">
                            <label>Chon mau xe:</label>
                            <select value={cars.selectedModel} onChange={this.changeModel}>
                                {cars.availableModels.map((model) => (
                                    <option key={model} value={model}>
                                        {model}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div className="control-group">
                            <label>Chon mau xe:</label>
                            <button onClick={this.changeColor}>Doi mau</button>
                        </div>
                        <div className="car-display">
                            <h3>Thong tin xe da chon</h3>
                            <p><strong>Hang:</strong> {cars.selectedBrand}</p>
                            <p><strong>Model:</strong> {cars.selectedModel}</p>
                            <div className="car-box"
                                style={{ backgroundColor: cars.selectedColor }}>
                                Mau: {cars.selectedColor.toUpperCase()}
                            </div>
                        </div>
                    </div>
                )}
            </div>
        );
    }
}

export default CarSearchApp;