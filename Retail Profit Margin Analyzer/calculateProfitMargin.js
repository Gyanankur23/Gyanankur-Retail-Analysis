const fs = require('fs');
const csv = require('csv-parser');

const categoryMargins = {};

fs.createReadStream('Gyanankur_Retail.csv')
  .pipe(csv())
  .on('data', (row) => {
    const cost = parseFloat(row.Amount);
    const revenue = parseFloat(row.Total_Amount);
    const category = row.Product_Category || 'Unknown Category';
    const subcategory = row.Product_Type || 'Unknown Type';
    const key = `${category} > ${subcategory}`;

    if (!isNaN(cost) && !isNaN(revenue) && revenue !== 0) {
      const margin = ((revenue - cost) / revenue) * 100;

      if (!categoryMargins[key]) {
        categoryMargins[key] = { totalMargin: 0, count: 0 };
      }

      categoryMargins[key].totalMargin += margin;
      categoryMargins[key].count += 1;
    }
  })
  .on('end', () => {
    const summary = Object.entries(categoryMargins).map(([key, data]) => ({
      Category_Subcategory: key,
      Avg_Profit_Margin: (data.totalMargin / data.count).toFixed(2) + '%',
      Entries: data.count
    }));

    const header = 'Category_Subcategory,Avg_Profit_Margin,Entries\n';
    const rows = summary
      .map(row => `${row.Category_Subcategory},${row.Avg_Profit_Margin},${row.Entries}`)
      .join('\n');

    fs.writeFile('profit_summary.csv', header + rows, (err) => {
      if (err) {
        console.error('Error writing file:', err);
      } else {
        console.log('✅ Summary saved to profit_summary.csv');
      }
    });

    console.table(summary);
  });
