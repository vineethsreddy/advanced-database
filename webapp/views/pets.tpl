<html>
    <body>
        <h1>List of Pets</h1>
        <ul>
        % for pet in pets:
            <li>{{pet['name'] + ' - ' + pet['kind']}}</li>
        % end
        </ul>
        <h1>Table of Pets</h1>
        <table>
        % for pet in pets:
            <tr>
                <td>{{pet['name']}}</td>
                <td>{{pet['kind']}}</td>
            <tr>
        % end
        </table>
    </body>
</html>