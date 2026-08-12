import "./hero.css"

export const Hero = () => {
  return (
    <div className="hero">
      <div className="hero__description">
        <div className="hero__title">
          <h1>Интернет как раньше
          дома и в телефоне</h1>
        </div>
        <div className="hero__subtitle">
          <p>YouTube, Instagram, Telegram и другие заблокированные
            сайты снова работают — на всех устройствах.
            Российские сайты и банки тоже. Всё в одной подписке.</p>
          <div className="hero__links">
            <a className="hero__link hero__link_background">Хочу такой — 8 900 ₽</a>
            <a className="hero__link hero__link_border">Попробовать только VPN</a>
          </div>
        </div>
      </div>
      <div className="hero__image"></div>
    </div>
  )
}
