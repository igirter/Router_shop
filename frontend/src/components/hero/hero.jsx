import './Hero.css'

export function Hero() {
  return (
    <section className="hero" id="hero">
      <div className="container hero__container">
        <div className="hero__content">
          <span className="hero__label">
            ИГРОВЫЕ МАРШРУТИЗАТОРЫ
          </span>

          <h1 className="hero__title">
            Играй без лагов.
            <br />
            Побеждай без ограничений.
          </h1>

          <p className="hero__description">
            Мощные маршрутизаторы для стабильного соединения,
            низкого ping и комфортной игры.
          </p>

          <a className="hero__button" href="#catalog">
            Смотреть каталог
          </a>
        </div>

        <div className="hero__visual">
          <div className="hero__glow" />

          <div className="hero__image-wrapper">
            <img
              className="hero__image"
              src="/router-hero.png"
              alt="Игровой маршрутизатор"
            />
          </div>
        </div>
      </div>
    </section>
  )
}