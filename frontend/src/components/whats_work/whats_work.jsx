import "./whats_work.css"
import logo from './assets/logo.svg'

const cards = [
  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home'},
  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home' },
  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home' },
  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home' },
  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home' },

  { image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSPwGPxV6aX9AcKq9kHpiv0ukvVdiJd6INIeN72sDsr8E4D71rcALXJ2Lo&s=10', name: 'Home' },
];

export const WhatsWork = () => {
  return (
    <div className="whats_work">
      <div className="whats_work__title">
        <h2>Снова работает всё</h2>
        <p>Открывается само, на всех устройствах.</p>
      </div>
      <div className="whats_work__cards">
        {cards.map((card, index) => (
            <div key={index}>
<img src={card.image} />
            </div>
        ))}
      </div>
      <div className="whats_work__cards_bottom"></div>
    </div>
  )
}
