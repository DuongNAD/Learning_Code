import React from "react";

function UserBio({bio}){
    return(
        <div className="user-bio">
            <h3>Gioi thieu</h3>
            <p>{bio}</p>
        </div>
    );
}
export default UserBio;