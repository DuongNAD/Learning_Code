import React from "react";
import UserInfo from "./UserInfo";
import UserBio from "./UserBio";


function UserProfile({user}){
    return(
        <div className="user-profile">
            <UserInfo name={user.name} email={user.email} />
            <UserBio bio={user.bio} />
        </div>
    );
}

export default UserProfile;