import React, {Component} from "react";
import RentalDetails from './RentalDetails'; 

class Rental extends Component{
    constructor(props){
        super(props);
        this.dailyRates = {
            Toyota: 50,
            Audi:70,
            Porche:100,
        };

        this.state = {
            carBrand: "Toyota",
            rentalDays: 1,
            totalCost: this.dailyRates['Toyota'] * 1,
        };
    }

    updateRentalInfo =(brand,days)=>{
        const cost = this.dailyRates[brand] * days;
        this.setState({
            carBrand: brand,
            rentalDays: days,
            totalCost: cost,
        });
    }

    handleBrandChange = (e) => {
        const newBrand = e.target.value;
        this.updateRentalInfo(newBrand, this.state.rentalDays);
    }

    handleDaysChange = (e) => {
        const newDays = parseInt(e.target.value);
        this.updateRentalInfo(this.state.carBrand, newDays);
    }

     render(){
        const {carBrand, rentalDays, totalCost} = this.state;
        const carOptions = Object.keys(this.dailyRates);
        const dayOptions =  [1,2,3,,4,5,6,7,8,9,10];
        
        return(
            <div className="rental-container">
                <h1>Thue xe</h1>
                <div className="controls">
                    <div className="control-group">
                        <label>Chon hang xe:</label>
                        <select id="car-brand" value={carBrand} onChange={this.handleBrandChange}>
                            {carOptions.map((brand => (
                                <option key={brand} value={brand}>{brand}</option>
                            )))}
                        </select>
                    </div>

                    <div className="control-group">
                        <label htmlFor="rental-days">So ngay thue:</label>
                        <select id="rental-days" value={rentalDays} onChange={this.handleDaysChange}>
                            {dayOptions.map(day =>(
                                <option key={day} value={day}>{day}</option>

                            ))}
                        </select>
                    </div>
                </div>

                <RentalDetails
          brand={carBrand}
          days={rentalDays}
          cost={totalCost}
        />
            </div>
        );
     }
}

export default Rental;