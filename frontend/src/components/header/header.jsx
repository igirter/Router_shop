import "./header.css"
import Logo from "./assets/pngegg (1).png"
const hrefs = [
  { name: 'Home', link: '#home' },
  { name: 'About', link: '#about' },
  { name: 'Contact', link: '#contact' },
];

const Header = () => {
  return (
    <header className="header">
      <div className="header__content">
        <nav className="header__nav">
          <ul>
          {hrefs.map((href, index) => (
              <li key={index}>
                  <a href={href.link}>{href.name}</a>
              </li>
          ))}
        </ul>
        </nav>
      </div>
      <div className="header__content cormorant-garamond">
        <img src={Logo}></img>
        <h3>Router</h3>
      </div>
      <div className="header__content">
      <a href="" className="header__link header__link_border">Войти</a>
      <a href="" className="header__link header__link_background">Заказать</a>
      </div>
    </header>
  )
}

export default Header;
