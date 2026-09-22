<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>

<%-- Xử lý lấy ngôn ngữ từ tham số URL ?local= và lưu vào session --%>
<c:if test="${not empty param.local}">
    <c:set var="currentLocale" value="${param.local}" scope="session" />
</c:if>
<c:if test="${empty sessionScope.currentLocale}">
    <c:set var="currentLocale" value="en_US" scope="session" />
</c:if>

<%-- Áp dụng Locale và gọi file properties (messages) --%>
<fmt:setLocale value="${sessionScope.currentLocale}" />
<fmt:setBundle basename="messages" />

<!DOCTYPE html>
<html>
<head>
    <title><fmt:message key="title.page"/></title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
        }
        .container {
            width: 600px;
            margin: 0 auto;
            text-align: center;
        }
        .lang-links { 
            margin-top: 20px; 
            margin-bottom: 30px;
        }
        .lang-links a { 
            margin: 0 10px; 
            color: #c71585; /* Màu hồng giống trong screenshot */
            text-decoration: none; 
            font-size: 14px;
        }
        .lang-links a:hover { 
            text-decoration: underline; 
        }
        h2 { 
            text-align: center; 
            font-family: "Times New Roman", Times, serif;
            font-size: 24px;
        }
        table { 
            margin: auto; 
            text-align: left;
            font-size: 14px;
        }
        td { 
            padding: 5px; 
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Links đổi ngôn ngữ -->
        <div class="lang-links">
            <a href="index.jsp?local=vi_VN"><fmt:message key="link.vietnamese"/></a>
            <a href="index.jsp?local=en_US"><fmt:message key="link.english"/></a>
        </div>

        <!-- Tiêu đề form -->
        <h2><fmt:message key="form.title"/></h2>

        <!-- Form nhập liệu -->
        <form>
            <table>
                <tr>
                    <td><fmt:message key="form.name"/></td>
                    <td><input type="text" name="name" size="25"></td>
                </tr>
                <tr>
                    <td><fmt:message key="form.gender"/></td>
                    <td>
                        <input type="radio" name="gender" value="male" id="male"> <label for="male"><fmt:message key="form.gender.male"/></label>
                        <input type="radio" name="gender" value="female" id="female"> <label for="female"><fmt:message key="form.gender.female"/></label>
                    </td>
                </tr>
                <tr>
                    <td><fmt:message key="form.birthday"/></td>
                    <td><input type="text" name="birthday" size="25"></td>
                </tr>
                <tr>
                    <td><fmt:message key="form.address"/></td>
                    <td><input type="text" name="address" size="25"></td>
                </tr>
                <tr>
                    <td><button type="submit"><fmt:message key="form.button.process"/></button></td>
                    <td><button type="reset"><fmt:message key="form.button.reset"/></button></td>
                </tr>
            </table>
        </form>
    </div>
</body>
</html>
