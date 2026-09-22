<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%@ taglib uri="jakarta.tags.fmt" prefix="fmt" %>

<%-- Handle I18N Localization --%>
<c:set var="lang" value="${not empty param.lang ? param.lang : not empty sessionScope.lang ? sessionScope.lang : 'en'}" scope="session" />
<fmt:setLocale value="${lang}" />
<fmt:setBundle basename="messages" />

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title><fmt:message key="form.title"/></title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; margin-top: 20px; }
        td { padding: 10px; }
        .error { color: red; font-weight: bold; margin-bottom: 10px; }
        .lang-switch { text-align: right; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="lang-switch">
        <a href="?lang=en">English</a> | <a href="?lang=vi">Tiếng Việt</a>
    </div>
    
    <h2><fmt:message key="form.title"/></h2>
    <a href="home">Home</a>
    <hr>
    
    <c:if test="${not empty error}">
        <div class="error"><fmt:message key="form.error.price" /></div>
    </c:if>

    <form action="insert" method="post">
        <table>
            <tr>
                <td><fmt:message key="form.name"/>:</td>
                <td><input type="text" name="name" value="${param.name}" required /></td>
            </tr>
            <tr>
                <td><fmt:message key="form.price"/>:</td>
                <td><input type="text" name="price" value="${param.price}" required /></td>
            </tr>
            <tr>
                <td><fmt:message key="form.warranty"/>:</td>
                <td><input type="text" name="warranty" value="${param.warranty}" /></td>
            </tr>
            <tr>
                <td><fmt:message key="form.accessories"/>:</td>
                <td><input type="text" name="accessories" value="${param.accessories}" /></td>
            </tr>
            <tr>
                <td><fmt:message key="form.stock"/>:</td>
                <td>
                    <label>
                        <input type="radio" name="inOutStock" value="true" ${param.inOutStock == 'true' or empty param.inOutStock ? 'checked' : ''} /> 
                        <fmt:message key="form.yes"/>
                    </label>
                    <label>
                        <input type="radio" name="inOutStock" value="false" ${param.inOutStock == 'false' ? 'checked' : ''} /> 
                        <fmt:message key="form.no"/>
                    </label>
                </td>
            </tr>
            <tr>
                <td><fmt:message key="form.image"/>:</td>
                <td><input type="text" name="image" value="${param.image}" /></td>
            </tr>
            <tr>
                <td colspan="2"><input type="submit" value="<fmt:message key='form.submit'/>" /></td>
            </tr>
        </table>
    </form>
</body>
</html>
