import './App.css'
import { Header } from './components/Header/Header'
import { Hero } from './components/Hero/Hero'
import { Catalog } from './components/Catalog/Catalog'
import { useEffect, useState } from 'react'

function App() {
const [products, setProducts] = useState([])

useEffect(() => {
  fetch('/api/products')
  .then((response) => response.json())
  .then((data) => {
    setProducts(data)
  })
}, [])

  return (
    <div className="app">
      <Header />

      <main>
        <Hero />
        <Catalog products={products} />
      </main>
    </div>
  )
}

export default App