import React from "react";
import { Link } from "react-router-dom";
const About = () => {
  return (
    <div className="about-container">
      <h2 className="about-title">Về Chúng Tôi</h2>
      <p className="about-text">
        Chào mừng bạn đến với dự án React của chúng tôi! Đây là nơi chúng tôi học tập,
        thử nghiệm và xây dựng các ứng dụng web hiện đại bằng thư viện React.
      </p>
      <p className="about-text">
        Mục tiêu của khóa học này là giúp các bạn nắm vững các khái niệm cốt lõi của React,
        từ component, props, state cho đến các hook nâng cao và quản lý trạng thái ứng dụng.
      </p>
      <h3 className="about-subtitle">Sứ mệnh của chúng tôi</h3>
      <p className="about-text">
        Sứ mệnh của chúng tôi là cung cấp một lộ trình học tập rõ ràng,
        thực tế và đầy cảm hứng cho tất cả mọi người đam mê lập trình front-end.
      </p>
    </div>
  );
};

export default About;