import React from "react";

const StockHistory = function(props) {
  return (
    <div className="customers--list">
      <table
        className="table w3-table w3-striped w3-border w3-centered w3-hoverable w3-card-4"
      >
        <thead key="thead">
          <tr>
            <th>ID</th>
            <th>Reference</th>
            <th>Type of Operation</th>
            <th>Contract Date</th>

            
          </tr>
        </thead>
        <tbody>
          {props.stockList.map(c => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.field_20}</td>
              <td>{c.field_22a}</td>
              <td>{c.field_30t}</td>
             
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StockHistory;
