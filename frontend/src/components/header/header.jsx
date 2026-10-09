import { useEffect, useState } from 'react'
import './Header.css'

const navItems = [
  {
    label: 'Главная',
    href: '#hero',
  },
  {
    label: 'Каталог',
    href: '#catalog',
  },
  {
    label: 'Преимущества',
    href: '#advantages',
  },
  {
    label: 'Контакты',
    href: '#contacts',
  },
]

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  useEffect(() => {
    document.body.style.overflow = isMenuOpen ? 'hidden' : ''

    return () => {
      document.body.style.overflow = ''
    }
  }, [isMenuOpen])

  const closeMenu = () => {
    setIsMenuOpen(false)
  }

  const toggleMenu = () => {
    setIsMenuOpen((prev) => !prev)
  }

  return (
    <header className="header">
      <div className="container">
        <a
          className="header__logo"
          href="#hero"
          onClick={closeMenu}
        >
          <img
            className="header__logo-image"
            src="/game-router-logo.png"
            alt="Game Router"
          />
        </a>

        <nav
          className={`header__nav ${
            isMenuOpen ? 'header__nav--open' : ''
          }`}
        >
          <ul className="header__list">
            {navItems.map((item) => (
              <li key={item.href} className="header__item">
                <a
                  className="header__link"
                  href={item.href}
                  onClick={closeMenu}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <button
          className={`header__burger ${
            isMenuOpen ? 'header__burger--active' : ''
          }`}
          type="button"
          onClick={toggleMenu}
          aria-label={isMenuOpen ? 'Закрыть меню' : 'Открыть меню'}
          aria-expanded={isMenuOpen}
        >
          <span />
          <span />
          <span />
        </button>
      </div>
    </header>
  )
}