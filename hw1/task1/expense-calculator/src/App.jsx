import { useState } from 'react'
import './App.css'

function App() {
  const [expenses, setExpenses] = useState([
    { category: '', amount: '' },
  ])
  const [results, setResults] = useState(null)

  const handleExpenseChange = (index, field, value) => {
    const newExpenses = expenses.map((exp, i) =>
      i === index ? { ...exp, [field]: value } : exp
    )
    setExpenses(newExpenses)
  }

  const addExpenseRow = () => {
    setExpenses([...expenses, { category: '', amount: '' }])
  }

  const calculateResults = () => {
    const validExpenses = expenses
      .filter(exp => exp.category && exp.amount && !isNaN(Number(exp.amount)))
      .map(exp => ({ ...exp, amount: Number(exp.amount) }))
    const total = validExpenses.reduce((sum, exp) => sum + exp.amount, 0)
    const avgDaily = total / 30
    const top3 = [...validExpenses]
      .sort((a, b) => b.amount - a.amount)
      .slice(0, 3)
    setResults({
      total,
      avgDaily,
      top3,
    })
  }

  return (
    <div className="container">
      <h1>Expense Calculator</h1>
      <div className="expense-table">
        <div className="table-header">
          <span>Category</span>
          <span>Amount ($)</span>
        </div>
        {expenses.map((exp, idx) => (
          <div className="table-row" key={idx}>
            <input
              type="text"
              placeholder="e.g. Groceries"
              value={exp.category}
              onChange={e => handleExpenseChange(idx, 'category', e.target.value)}
            />
            <input
              type="number"
              placeholder="e.g. 15000"
              value={exp.amount}
              min="0"
              onChange={e => handleExpenseChange(idx, 'amount', e.target.value)}
            />
          </div>
        ))}
        <button className="add-row" onClick={addExpenseRow}>+ Add Expense</button>
      </div>
      <button className="calculate-btn" onClick={calculateResults}>Calculate</button>
      {results && (
        <div className="results">
          <h2>Results</h2>
          <p><strong>Total amount of expenses:</strong> ${results.total.toLocaleString()}</p>
          <p><strong>Average daily expense:</strong> ${results.avgDaily.toLocaleString(undefined, { maximumFractionDigits: 2 })}</p>
          <p><strong>Top 3 expenses:</strong> {results.top3.map((exp, i) => `${exp.category} ($${exp.amount.toLocaleString()})`).join(', ')}</p>
        </div>
      )}
    </div>
  )
}

export default App
