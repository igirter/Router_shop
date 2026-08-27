import Header from './components/header/header.jsx'
import { Hero } from './components/hero/hero.jsx'
import './App.css'
import { WhatsWork } from './components/whats_work/whats_work.jsx'

function App() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <Header />
      <Hero />
      <WhatsWork />
    </>
  )
}

export default App
