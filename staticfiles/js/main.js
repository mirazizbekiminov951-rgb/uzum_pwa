const uzb = document.getElementById('uzb');
const rus = document.getElementById('rus');

uzb.addEventListener('click', (e) => {
    e.stopPropagation();
    rus.classList.toggle('hidden');
});


document.addEventListener('click', () => {
    rus.classList.add('hidden');
});


const Ochish = document.getElementById('ochish');
const Yopish = document.getElementById('yopish'); 
const OrqaFoni = document.getElementById('orqafon');
const shaharlar = document.getElementById('shaharlar');

const modalniOchish = () => {
    shaharlar.classList.remove('hidden');
    document.body.style.overflow = 'hidden'; 
};

const modalniYopish = () => {
    shaharlar.classList.add('hidden');
    document.body.style.overflow = ''; 
};

Ochish.addEventListener('click', modalniOchish);
Yopish.addEventListener('click', modalniYopish);
OrqaFoni.addEventListener('click', modalniYopish); 


const qidiruv = document.querySelector('#shaharlar input[type="text"]');
const shahar = document.querySelectorAll('#shaharlar .overflow-y-auto button');

qidiruv.addEventListener('input', (e) => {
    const qidiruvMatni = e.target.value.toLowerCase().trim();

    shahar.forEach(tugma => {
        const shaharNomi = tugma.querySelector('span').textContent.toLowerCase();
        
        if (shaharNomi.includes(qidiruvMatni)) {
            tugma.classList.remove('hidden'); 
        } else {
            tugma.classList.add('hidden');    
        }
    });
});


const span = Ochish.querySelector('span');

shahar.forEach(tugma => {
    tugma.addEventListener('click', () => {
        const tanlanganShahar = tugma.querySelector('span').textContent;
        span.textContent = tanlanganShahar; 
        modalniYopish(); 
    });
});


        document.addEventListener('DOMContentLoaded', function () {
            const btn = document.getElementById('catalogBtn');
            const content = document.getElementById('catalogContent');
            if (!btn || !content) return;
            btn.addEventListener('click', () => {
                content.classList.toggle('hidden');
            });
        });
 new Swiper(".bannerSwiper", {
            loop: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        });
        new Swiper(".categorySwiper", {
            spaceBetween: 12,
            breakpoints: {
                0: {
                    slidesPerView: 1.2,
                },
                480: {
                    slidesPerView: 1.8,
                },
                640: {
                    slidesPerView: 2.3,
                },
                768: {
                    slidesPerView: 3,
                },
                1024: {
                    slidesPerView: 4,
                }
            }
        });